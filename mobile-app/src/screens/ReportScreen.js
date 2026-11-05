import React from 'react';
import { View, Text, Button } from 'react-native';

export default function ReportScreen() {
  return (
    <View>
      <Text>Sauti Community – Tap to Report in Hausa/English</Text>
      <Text>Example: 'Yau a unguwa goma suna zawo' (10 with diarrhoea)</Text>
      <Button title="Record 30 sec Voice" onPress={() => {}} />
    </View>
  );
}