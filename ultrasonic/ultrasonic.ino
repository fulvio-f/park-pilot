int trigPin = 11;
int echoPin = 12;
int ping;

void setup() {

  Serial.begin(9600);
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin,INPUT);
}

void loop() {

  digitalWrite(trigPin,LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  ping = pulseIn(echoPin,HIGH);
  delay(25);
  Serial.println(ping);
}
