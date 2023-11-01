import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Fruit Detector'),
        ),
        body: Container(
          alignment: AlignmentDirectional.center,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              const SizedBox(
                height: 50,
                child: Text(
                  'Click to start scanning',
                  style: TextStyle(fontSize: 24),
                ),
              ),
              FloatingActionButton.extended(
                onPressed: () {},
                label: const Text('Scanner'),
                icon: const Icon(Icons.camera_alt),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
