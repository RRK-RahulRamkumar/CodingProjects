let sequence = [0, 1];

let x = Number(prompt("Enter the number of additions:"));

// Main program

let index = 0;

for (let i = 0; i < x; i++) {
    sequence.push(sequence[index] + sequence[index + 1]);
    index = index + 1;

};

alert(sequence);