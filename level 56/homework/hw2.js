let array = [];

for (let i = 0; i < 10; i++) {
    let num = parseInt(prompt(`შეიყვანეთ ${i + 1}-ე რიცხვი:`));
    array.push(num);
}

for (let i = 0; i < array.length; i++) {
    array[i] *= 2;
}

console.log("გაორმაგებული მასივი:");
console.log(array);