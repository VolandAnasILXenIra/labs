const int PIN_TRIG = 8;
const int PIN_ECHO = A0;
const int PIN_TRIG_2 = 9;
const int PIN_ECHO_2 = A1;
const int PIN_TRIG_3 = 10;
const int PIN_ECHO_3 = A2;
const int PIN_TRIG_4 = 11;
const int PIN_ECHO_4 = A3;
const int BUTTON_PIN1 = 5;
const int BUTTON_PIN2 = 4;
const int BUTTON_PIN3 = 3;
const int BUTTON_PIN4 = 2;


// Функция для измерения расстояния
unsigned long measureDistance(int PIN_TRIG, int PIN_ECHO) {
digitalWrite(PIN_TRIG, LOW);
delayMicroseconds(2);
digitalWrite(PIN_TRIG, HIGH);
delayMicroseconds(10);
digitalWrite(PIN_TRIG, LOW);

unsigned long duration = pulseIn(PIN_ECHO, HIGH);
unsigned long distance = duration * 0.034 / 2;

return distance;
}

void setup() {
// Инициализация пинов для ультразвуковых датчиков в качестве выводов
pinMode(PIN_TRIG, OUTPUT);
pinMode(PIN_ECHO, INPUT);
pinMode(PIN_TRIG_2, OUTPUT);
pinMode(PIN_ECHO_2, INPUT);
pinMode(PIN_TRIG_3, OUTPUT);
pinMode(PIN_ECHO_3, INPUT);
pinMode(PIN_TRIG_4, OUTPUT);
pinMode(PIN_ECHO_4, INPUT);

// Инициализация пинов для кнопок в качестве входов
pinMode(BUTTON_PIN1, INPUT);
pinMode(BUTTON_PIN2, INPUT);
pinMode(BUTTON_PIN3, INPUT);
pinMode(BUTTON_PIN4, INPUT);

// Инициализация серийного порта для вывода данных
Serial.begin(9600);
}

void loop() {
// Получение расстояния от каждого датчика и состояния каждой кнопки
unsigned long distance1 = measureDistance(PIN_TRIG, PIN_ECHO);
unsigned long distance2 = measureDistance(PIN_TRIG_2, PIN_ECHO_2);
unsigned long distance3 = measureDistance(PIN_TRIG_3, PIN_ECHO_3);
unsigned long distance4 = measureDistance(PIN_TRIG_4, PIN_ECHO_4);

int buttonState1 = digitalRead(BUTTON_PIN1);
int buttonState2 = digitalRead(BUTTON_PIN2);
int buttonState3 = digitalRead(BUTTON_PIN3);
int buttonState4 = digitalRead(BUTTON_PIN4);

// Вывод расстояний в монитор последовательного порта
Serial.print("Distance 1: ");
Serial.print(distance1);
Serial.println(" cm");

Serial.print("Distance 2: ");
Serial.print(distance2);
Serial.println(" cm");

Serial.print("Distance 3: ");
Serial.print(distance3);
Serial.println(" cm");

Serial.print("Distance 4: ");
Serial.print(distance4);
Serial.println(" cm");

// Вывод состояний кнопок
Serial.print("Button 1: ");
Serial.println(buttonState1);

Serial.print("Button 2: ");
Serial.println(buttonState2);

Serial.print("Button 3: ");
Serial.println(buttonState3);

Serial.print("Button 4: ");
Serial.println(buttonState4);

// Задержка между измерениями
delay(500);
}
