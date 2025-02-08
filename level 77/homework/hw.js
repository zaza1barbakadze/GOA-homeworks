function createObjectFromArrays(keys, values) {
    const obj = {};

    for (let i = 0; i < keys.length; i++) {
        obj[keys[i]] = values[i];
    }

    return obj;
}

const keys = ["id", "name", "email"];
const values = [1, "Luka", "luka@gmail.com"];

console.log(createObjectFromArrays(keys, values));