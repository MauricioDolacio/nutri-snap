import 'package:flutter/material.dart';
import 'package:fruit_detec/components/models/nutrition_model.dart';

class NutritionWidget extends StatelessWidget {
  final NutritionModel? nutritionModel;

  const NutritionWidget({Key? key, required this.nutritionModel})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Card(
        margin: const EdgeInsets.all(16.0),
        child: Padding(
          padding: const EdgeInsets.fromLTRB(16.0, 16.0, 16.0, 8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              const Text(
                'NUTRITION FACTS',
                style: TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 18.0,
                ),
              ),
              const SizedBox(height: 8.0),
              Text(
                '${nutritionModel?.food?.toUpperCase()}',
                style: const TextStyle(
                  fontWeight: FontWeight.bold,
                  fontSize: 16.0,
                ),
              ),
              const SizedBox(height: 8.0),
              const Text('Serving Size 100g'),
              const SizedBox(height: 12.0),
              Table(
                border: TableBorder.all(color: Colors.grey),
                children: [
                  _buildTableRow('Energy Kcal',
                      '${nutritionModel?.kcal!.total}${nutritionModel?.kcal!.unit}'),
                  _buildTableRow('Carb',
                      '${nutritionModel?.carb!.total}${nutritionModel?.carb!.unit}'),
                  _buildTableRow('Protein',
                      '${nutritionModel?.protein!.total}${nutritionModel?.protein!.unit}'),
                  _buildTableRow('Total Fat',
                      '${nutritionModel?.totalFat!.total}${nutritionModel?.totalFat!.unit}'),
                  _buildTableRow('Saturated Fat',
                      '${nutritionModel?.fatSat!.total}${nutritionModel?.fatSat!.unit}'),
                  _buildTableRow('Sodium',
                      '${nutritionModel?.sodium!.total}${nutritionModel?.sodium!.unit}'),
                  _buildTableRow('Vit A',
                      '${nutritionModel?.vitA!.total}${nutritionModel?.vitA!.unit}'),
                  _buildTableRow('Vit B6',
                      '${nutritionModel?.vitB6!.total}${nutritionModel?.vitB6!.unit}'),
                  _buildTableRow('Vit C',
                      '${nutritionModel?.vitC!.total}${nutritionModel?.vitC!.unit}'),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  TableRow _buildTableRow(String label, String value) {
    return TableRow(
      children: [
        TableCell(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              label,
              style: const TextStyle(fontWeight: FontWeight.bold),
            ),
          ),
        ),
        TableCell(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(value),
          ),
        ),
      ],
    );
  }
}
