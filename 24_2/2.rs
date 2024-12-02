use std::fs::File;
use std::io::{self, BufRead};

fn is_increasing_decreasing(vec_arr: &Vec<i32>) -> bool {
    let mut sorted_arr = vec_arr.clone();
    sorted_arr.sort();

    if vec_arr == &sorted_arr {
        return true;
    }

    let mut reversed_arr = sorted_arr.clone();
    reversed_arr.reverse();

    if vec_arr == &reversed_arr {
        return true;
    }

    false
}

fn is_diff_1_2(arr: &Vec<i32>) -> bool {
    for i in 0..arr.len() - 1 {
        let diff = (arr[i] - arr[i + 1]).abs();
        if diff < 1 || diff > 3 {
            return false;
        }
    }
    true
}

fn can_it_be_safe(arr: &Vec<i32>) -> bool {
    for i in 0..arr.len() {
        let mut new_arr = arr.clone();
        new_arr.remove(i);
        if is_diff_1_2(&new_arr) && is_increasing_decreasing(&new_arr) {
            return true;
        }
    }
    false
}

fn main() -> io::Result<()> {
    let file = File::open("2.txt")?; // Replace "file.txt" with your file path
    let reader = io::BufReader::new(file);
    let mut is_safe = 0;

    for line in reader.lines() {
        let line = line?; // Unwrap the Result to get the line
        let numbers: Vec<i32> = line
            .split_whitespace() // Split the line by whitespace
            .filter_map(|num| num.parse::<i32>().ok()) // Parse each part as an i32, ignoring invalid parts
            .collect(); // Collect parsed numbers into a vector
        if is_diff_1_2(&numbers) && is_increasing_decreasing(&numbers) {
            is_safe += 1;
        } else {
            if can_it_be_safe(&numbers) {
                is_safe += 1;
            }
        }
    }
    println!("{}", is_safe);
    Ok(())
}
