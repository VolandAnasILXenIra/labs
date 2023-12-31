import processing.serial.*;
Serial myPort;
String resultString; // Строчная переменная для результатов

float leftPaddle, rightPaddle;//переменные для значений // датчихов иѕгиба
int resetButton, serveButton; // переменные для кнопок
int leftPaddleX, rightPaddleX;//горизонтальные позиции
// рахетох
int paddleHeight = 50; // вертихальный размер ракеток
int paddleWidth = 10; // горизонтальный размер ракеток
float leftMinimum = 10; // минимальное значение левого
// датчика изгиба
float rightMinimum=10;//минимальное значение правого
// датчиха иѕгиба
float leftMaximum = 130; // максимальное значение левого
// датчика изгиба
float rightMaximum = 630; // максимальное значение правого

int ballSize=10;//рaзмер мячикa
int xDirection=1;//горизонтaльное нaпрaвление движения // мячикa
// влево: –1, впрaво: 1
int yDirection = 1; // вертикaльное нaпрaвление движения // мячикa
int xPos, yPos;
// вверх: –1, вниз: 1
//горизонтaльное и вертикaльное // положение мячикa

boolean ballInMotion=false;//мячик движется?
int leftScore = 0;
int rightScore = 0;

int fontSize = 36; // размер шрифта для отображения счета

void setup(){
size(640, 280); // устанавливаем размер окна апплета
String portName = Serial.list()[0];
// открываем последовательный порт:
myPort = new Serial(this, portName, 9600);
// считываем байты в буфер, пока не дойдем до // символа перевода строки (ASCII 10):
myPort.bufferUntil('\n');
// инициализируем значения датчиков:
leftPaddle = height/2;
rightPaddle = height/2;
resetButton = 0;
serveButton = 0;
// инициализируем горизонтальные позиции ракеток:
leftPaddleX = 50;
rightPaddleX = width - 50;
// рисуем фигуры беѕ окантовки:
noStroke();
xPos = width/2;
yPos = height/2;
// соѕдаем mрифт иѕ третьего mрифта, доступного системе:
PFont myFont = createFont(PFont.list()[2], fontSize);
textFont(myFont);
}

void serialEvent(Serial myPort){
// считываем данные иѕ последовательного буфера:
String inputString = myPort.readStringUntil('\n');
// отбрасываем символы возврата ракетки и перевода строки
// иѕ строки ввода:
inputString = trim(inputString);
// очищаем переменную resultString:
resultString = "";
// разделяем входную строку по запятым и преобразовываем
// полученные фрагменты в целые числа:
int sensors[] = int(inputString.split(","));

// если получены все строки значений датчиков, используем их:
if (sensors.length == 4) {
// масmтабируем данные датчихов иѕгиба х диапаѕону // рахетох:
leftPaddle = map(sensors[0], leftMinimum, leftMaximum, 0, height);
rightPaddle = map(sensors[1], rightMinimum, rightMaximum, 0, height);
// присваиваем ѕначения хнопох соответствующим // переменным:
resetButton = sensors[2];
serveButton = sensors[3];
// добавляем ѕначения х строхе реѕультата:
resultString += "left: "+ leftPaddle + "\tright: " + rightPaddle;
resultString += "\treset: "+ resetButton + "\tserve: " + serveButton;
}
myPort.write('\r'); // посылаем символ воѕврата харетхи
}

void draw(){
// задаем цвет фона и заливки для окна апплета:
background(#044f6f);
fill(#ffffff);
// рисуем левую рахетху:
rect(leftPaddleX, leftPaddle, paddleWidth, paddleHeight);
// рисуем правую рахетху:
rect(rightPaddleX, rightPaddle, paddleWidth, paddleHeight);
// вычисляем местонахождение мячиха и прорисовываем его:
if(ballInMotion==true){
animateBall();
}
// если нажата хнопха подачи, ѕапусхаем мячих в движение:
if (serveButton == 1) {
ballInMotion = true;
}
//еслинажатахнопхасброса,обнуляемсчетиѕапусхаем // мячих в движение:
if (resetButton == 1) {
leftScore = 0;
rightScore = 0;
ballInMotion = true;
}
// выводим счет на Зхран:
text(leftScore, fontSize, fontSize);
text(rightScore, width-fontSize, fontSize);
}

void animateBall(){
// если мячих движется влево:
if (xDirection < 0) {
// если мячих нaходится слевa от левой рaхетхи
if ((xPos <= leftPaddleX)) {
// если мячих нaходится между верхом и ниѕом левой рaхетхи:
if((leftPaddle - (paddleHeight/2) <= yPos) && (yPos <=
leftPaddle + (paddleHeight /2))) {
// иѕменяем нaпрaвление гориѕонтaльного движения нa обрaтное:
xDirection =-xDirection;
}
}
}
// если мячих движется вправо:
else {
// если мячих справа от правой рахетхи
if ((xPos >= ( rightPaddleX + ballSize/2))) {
// если мячих находится между верхом и ниѕом // правой рахетхи:
if((rightPaddle - (paddleHeight/2) <=yPos) && (yPos <= rightPaddle + (paddleHeight /2))) {
// иѕменяем направление гориѕонтального
// движения на обратное:
xDirection =-xDirection;
}
}
}
// если мячих выходит ѕа пределы охна слева:
if (xPos < 0) {
rightScore++;
resetBall();
}
// если мячих выходит ѕа пределы охна справа:
if (xPos > width) {
leftScore++;
resetBall();
}
// не даем мячиху выйти ѕа верхний или нижний предел охна
if ((yPos - ballSize/2 < 0) || (yPos +ballSize/2 >height)) { // иѕменяем направление вертихального движения мячиха
// на обратное:
yDirection = -yDirection;
}
// обновляем местонахождение мячиха:
xPos = xPos + xDirection;
yPos = yPos + yDirection;
// рисуем мячих:
rect(xPos, yPos, ballSize, ballSize);
}

void resetBall() {
// воѕвращаем мячих обратно в центр охна:
xPos = width/2;
yPos = height/2;
}
