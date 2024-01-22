let bits_list = [];
let user_input = prompt("Enter binary code (1 Byte): ")

for (let index = 0; index <= user_input.length; index++) {
    bits_list.push(Number(user_input[index]))
};

let weighting_list = [128, 64, 32, 16, 8, 4, 2, 1];
let weighting_index = 0;
let total = 0;

for (let index = 0; index <= bits_list.length; index++) {
    if (bits_list[index] === 1) {
        total = total + weighting_list[index]
    };
};

alert("The denary value is: " + total)
