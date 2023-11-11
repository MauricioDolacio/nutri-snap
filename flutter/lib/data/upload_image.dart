import 'dart:convert';
import 'dart:io';
import 'package:fruit_detec/components/models/nutrition_model.dart';
import 'package:http/http.dart' as http;

Future<NutritionModel?> uploadImage(filepath, url) async {
  var request = http.MultipartRequest('POST', Uri.parse(url));

  request.files.add(http.MultipartFile('picture',
      File(filepath).readAsBytes().asStream(), File(filepath).lengthSync(),
      filename: filepath.split("/").last));

  try {
    var client = http.Client();
    var streamedResponse =
        await client.send(request).timeout(const Duration(seconds: 12));

    if (streamedResponse.statusCode == 200) {
      var dict = await utf8.decodeStream(streamedResponse.stream);
      return nutritionModelFromJson(dict);
    } else {
      return null;
    }
  } catch (e) {
    // Handle exceptions, e.g., timeout exception
    return null;
  }
}
