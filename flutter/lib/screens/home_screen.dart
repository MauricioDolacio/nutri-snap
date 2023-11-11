import 'package:flutter/material.dart';
import 'package:fruit_detec/components/widgets/loading_widget.dart';
import 'package:fruit_detec/components/models/nutrition_model.dart';
import 'package:fruit_detec/components/widgets/nutrition_widget.dart';
import 'package:fruit_detec/components/widgets/initial_widget.dart';
import 'package:fruit_detec/data/upload_image.dart';
import 'package:image_picker/image_picker.dart';

enum ScreenState {
  initial,
  loading,
  nutritionAvailable,
}

class Home extends StatefulWidget {
  const Home({Key? key}) : super(key: key);

  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {
  ImagePicker picker = ImagePicker();
  XFile? image;
  NutritionModel? _nutrition;
  ScreenState _screenState = ScreenState.initial;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text(
          "Snap Fruit",
          style: TextStyle(
            fontSize: 24.0,
          ),
        ),
        leading: IconButton(
          icon: const Icon(Icons.menu),
          onPressed: () {
            //TODO: Adicione o código que você deseja executar quando o botão de menu for pressionado
          },
        ),
      ),
      body: Container(
        alignment: FractionalOffset.center,
        child: _buildScreen(),
      ),
      bottomNavigationBar: BottomAppBar(
        shape: const CircularNotchedRectangle(),
        child: SizedBox(
          height: 50.0,
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              IconButton(
                icon: const Icon(Icons.camera_alt),
                onPressed: () async {
                  await captureAndUploadImage(ImageSource.camera);
                },
              ),
              IconButton(
                icon: const Icon(Icons.photo),
                onPressed: () async {
                  await captureAndUploadImage(ImageSource.gallery);
                },
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildScreen() {
    switch (_screenState) {
      case ScreenState.initial:
        return const InitialScreen();
      case ScreenState.loading:
        return const LoadingWidget();
      case ScreenState.nutritionAvailable:
        return NutritionWidget(nutritionModel: _nutrition!);
    }
  }

  Future<void> captureAndUploadImage(ImageSource source) async {
    try {
      image = await picker.pickImage(source: source);

      setState(() {
        _screenState = ScreenState.loading;
      });

      final NutritionModel? nutrition = await uploadImage(
        image!.path,
        'http://177.200.66.220:5000',
      );

      if (nutrition == null) {
        ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
          content: Text('Failed to load the image'),
        ));
        return;
      }

      setState(() {
        _nutrition = nutrition;
        _screenState = ScreenState.nutritionAvailable;
      });

      // You can place any additional logic here if needed
    } finally {
      if (_screenState != ScreenState.nutritionAvailable) {
        setState(() {
          _screenState = ScreenState.initial;
        });
      }
    }
  }
}
