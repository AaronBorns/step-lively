int nSensor = 6;
void setup() {
  Serial.begin(115200);
}

String Packet() {
  String packet;
  char SensorValue[nSensor + 1];
  SensorValue[0] = ',';
  for (int i=1; (i < nSensor+1); i++) {
    int Pin = {A0, A1, A2, A3, A4, A5};
    SensorValue[i] = map(Serial.read(Pin[i-1]), 0, 5, 0, 255);
  }
  packet = String(SensorValue);
  return packet;
}

void loop() {
  String packet = Packet();
  Serial.println(packet); 
}
