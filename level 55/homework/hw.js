let operacoin1 = prompt("ჩაწერეთ + ან -")
let operacoin2 = parseInt(prompt("ჩაწერეთ რაიმე რიცხვი"))
let operacoin3 = parseInt(prompt("ჩაწერეთ რაიმე რიცხვი"))

if (operacoin1 === "+"){
    alert(operacoin2 + operacoin3)
 }
else if (operacoin1 === "-"){
    alert(operacoin2 - operacoin3)
}
else{
    alert("პასუხი არასწორია")
}