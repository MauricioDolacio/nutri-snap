// To parse this JSON data, do
//
//     final nutritionModel = nutritionModelFromJson(jsonString);

import 'dart:convert';

NutritionModel nutritionModelFromJson(String str) => NutritionModel.fromJson(json.decode(str));

String nutritionModelToJson(NutritionModel data) => json.encode(data.toJson());

class NutritionModel {
  NutritionModel({
    this.carb,
    this.fatSat,
    this.food,
    this.kcal,
    this.protein,
    this.sodium,
    this.totalFat,
    this.vitA,
    this.vitB6,
    this.vitC,
  });

  Carb? carb;
  Carb? fatSat;
  String? food;
  Carb? kcal;
  Carb? protein;
  Carb? sodium;
  Carb? totalFat;
  Carb? vitA;
  Carb? vitB6;
  Carb? vitC;

  factory NutritionModel.fromJson(Map<String, dynamic> json) => NutritionModel(
    carb: Carb.fromJson(json["Carb"]),
    fatSat: Carb.fromJson(json["FatSAT"]),
    food: json["Food"],
    kcal: Carb.fromJson(json["Kcal"]),
    protein: Carb.fromJson(json["Protein"]),
    sodium: Carb.fromJson(json["Sodium"]),
    totalFat: Carb.fromJson(json["TotalFat"]),
    vitA: Carb.fromJson(json["VitA"]),
    vitB6: Carb.fromJson(json["VitB6"]),
    vitC: Carb.fromJson(json["VitC"]),
  );

  Map<String, dynamic> toJson() => {
    "Carb": carb!.toJson(),
    "FatSAT": fatSat!.toJson(),
    "Food": food,
    "Kcal": kcal!.toJson(),
    "Protein": protein!.toJson(),
    "Sodium": sodium!.toJson(),
    "TotalFat": totalFat!.toJson(),
    "VitA": vitA!.toJson(),
    "VitB6": vitB6!.toJson(),
    "VitC": vitC!.toJson(),
  };
}

class Carb {
  Carb({
    this.total,
    this.unit,
  });

  double? total;
  String? unit;

  factory Carb.fromJson(Map<String, dynamic> json) => Carb(
    total: json["total"].toDouble(),
    unit: json["unit"],
  );

  Map<String, dynamic> toJson() => {
    "total": total,
    "unit": unit,
  };
}
