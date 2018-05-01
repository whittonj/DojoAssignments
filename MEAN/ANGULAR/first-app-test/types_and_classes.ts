var myNum: number = 5;
var myString: string = "Hello Universe";
var myArr: number = [1,2,3,4];
var myObj = { name:'Bill'};
var anythingVariable:any = "Hey";
anythingVariable = 25; 
var arrayOne: boolean = [true, false, true, true]; 
var arrayTwo: any = [1, 'abc', true, 2];
var myObj = { x: 5, y: 10 };
// object constructor
//
//class MyNode {
//    function MyNode(val) {
//       this.val = 0;
//        this.val = val;
//    }
//    MyNode.prototype.doSomething = function () {
//        this._priv = 10;
//    };
//    return MyNode;
//}());
//myNodeInstance = new MyNode(1);
//console.log(myNodeInstance.val);

// end class constructor

function myFunction(message: string) {
    console.log(message);
    return;
}

function errorHandler(message: string): never{
	throw new Error(message);
}
