let list = [9, 1, 8, 2, 7, 3, 6, 4, 5];

let min_index = 0;
let cur_index = 0;
let save_cur_index = undefined;

for (let i = 0; i < list.length; i++) {
    let current_minimum = list[min_index];
    let original_minimum = list[min_index];

    while (cur_index < (list.length - 1)) {
        cur_index = cur_index + 1;
        let current_item = list[cur_index];

        if (current_minimum > current_item) {
            current_minimum = current_item;
            save_cur_index = cur_index;
        };
    };
    let var1 = original_minimum;
    let var2 = list[save_cur_index];
    list[min_index] = var2;
    list[save_cur_index] = var1;
    min_index = min_index + 1;
    cur_index = min_index;

};

console.log(list)