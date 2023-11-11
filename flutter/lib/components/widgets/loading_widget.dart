import 'package:flutter/material.dart';

class LoadingWidget extends StatefulWidget {
  const LoadingWidget({Key? key}) : super(key: key);

  @override
  _LoadingWidgetState createState() => _LoadingWidgetState();
}

class _LoadingWidgetState extends State<LoadingWidget> {
  bool _showText = false;

  @override
  void initState() {
    super.initState();
    Future.delayed(const Duration(seconds: 6), () {
      if (mounted) {
        setState(() {
          _showText = true;
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Container(
            alignment: Alignment.center,
            child: const CircularProgressIndicator(),
          ),
          const SizedBox(height: 16),
          AnimatedOpacity(
            opacity: _showText ? 1.0 : 0.0,
            duration: const Duration(milliseconds: 500),
            child: const Text(
              'Isso está demorando mais que o normal...',
              style: TextStyle(fontSize: 16),
            ),
          ),
        ],
      ),
    );
  }
}
