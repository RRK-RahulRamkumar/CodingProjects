let denary_number = Number(prompt("Enter a denary number:"));
let binary_weighting = [128, 64, 32, 16, 8, 4, 2, 1];
let binary_list = [];

if (denary_number <= 255) {
    for (let index = 0; index < binary_weighting.length; index++) {
        if (denary_number >= binary_weighting[index]) {
            denary_number = denary_number - binary_weighting[index];
            binary_list.push(1);
        } else {
            binary_list.push(0);
        };
    };
    alert(binary_list);
} else {
    alert("Denary number is greater than 255");
};