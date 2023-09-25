const int leftTrigPin = A0;
const int leftEchoPin = 2;
const int rightTrigPin = A1;
const int rightEchoPin = 3;
const int resetButton = 4;
const int serveButton = 5;

long leftDistance = 0;
long rightDistance = 0;
int resetReading = 0;
int serveReading = 0;

void setup() {
  Serial.begin(9600);
  pinMode(leftTrigPin, OUTPUT);
  pinMode(leftEchoPin, INPUT);
  pinMode(rightTrigPin, OUTPUT);
  pinMode(rightEchoPin, INPUT);
  pinMode(resetButton, INPUT);
  pinMode(serveButton, INPUT);
}

void loop() {
  leftDistance = readDistance(leftTrigPin, leftEchoPin);
  rightDistance = readDistance(rightTrigPin, rightEchoPin);
  
  resetReading = digitalRead(resetButton);
  serveReading = digitalRead(serveButton);

  Serial.print(leftDistance);
  Serial.print(',');
  Serial.print(rightDistance);
  Serial.print(',');
  Serial.print(resetReading);
  Serial.print(',');
  Serial.println(serveReading);
}

long readDistance(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  long distance = (duration/2) / 29.1;

  return distance;
}
