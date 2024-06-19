const fruits = ["corn", "mango","apple","pine","berry"]; 
const removed = fruits.splice(2, 2); // Mutates fruits and returns array of removed items
console.log('fruits', fruits); // ["mango","apple","berry"]
console.log('removed', removed); // ["pine"]

