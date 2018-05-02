var myNum = 5;
var myString = "Hello Universe";
var myArr = [1, 2, 3, 4];
var myObj = { name: 'Bill' };
var anythingVariable = "Hey";
anythingVariable = 25;
var arrayOne = [true, false, true, true];
var arrayTwo = [1, 'abc', true, 2];
var myObj = { x: 5, y: 10 };
// object constructor
var MyNode = /** @class */ (function () {
    function MyNode(val) {
        this.val = val;
    }
    MyNode.prototype.doSomething = function () {
        this._priv = 10;
    };
    return MyNode;
}());
var myNodeInstance = new MyNode(1);
console.log(myNodeInstance.val);
function myFunction() {
    console.log('Hello World');
    return;
}
function sendingErrors() {
    throw new Error('Error message');
}
function myFunction(message) {
    console.log(message);
    return;
}
function errorHandler(message) {
    throw new Error(message);
}
