int nSensor = 6;
int i;
//int t = 0; leave out time for now

String Packet(int s1, int s2, int s3, int s4, int s5, int s6); //function declaration

void setup() {
  Serial.begin(115200);
}

String Packet(int s1, int s2, int s3, int s4, int s5, int s6) {
  String packet;
  char SensorValue[nSensor + 1];
  int ArtificialSensor[nSensor] = {s1, s2, s3, s4, s5, s6};
  SensorValue[0] = ',';
  for (int i=1; (i < nSensor+1); i++) {
    SensorValue[i] = ArtificialSensor[i-1];
  }
  packet = String(SensorValue);
  return packet;
}

void loop() {
  int s1 = random(101,110);
  int s2 = random(51,60);
  int s3 = random(61,70);
  int s4 = random(71,80);
  int s5 = random(81,90);
  int s6 = random(91,100);
  String packet = Packet(s1, s2 , s3, s4, s5, s6);
  if (packet.length() == 7) {
    Serial.println(packet);
  }
  else{
    exit(0);
  }
}

