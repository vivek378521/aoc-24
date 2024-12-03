use regex::Regex;
use std::fs;

fn main() {
    let file_path = "3.txt";

    let content = match fs::read_to_string(file_path) {
        Ok(data) => data,
        Err(err) => {
            eprintln!("Error reading file: {}", err);
            return;
        }
    };

    let do_pattern = Regex::new(r"do\(\)").unwrap();
    let dont_pattern = Regex::new(r"don't\(\)").unwrap();
    let mul_pattern = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    let mut is_enabled = true;

    let mut valid_mul = Vec::new();

    for cap in Regex::new(r"do\(\)|don't\(\)|mul\(\d+,\d+\)")
        .unwrap()
        .find_iter(&content)
    {
        let token = cap.as_str();

        if do_pattern.is_match(token) {
            is_enabled = true;
        } else if dont_pattern.is_match(token) {
            is_enabled = false;
        } else if mul_pattern.is_match(token) && is_enabled {
            if let Some(captures) = mul_pattern.captures(token) {
                let num1: i32 = captures[1].parse().unwrap();
                let num2: i32 = captures[2].parse().unwrap();
                valid_mul.push((num1, num2));
            }
        }
    }

    let mut total_mul = 0;

    for (x, y) in valid_mul {
        total_mul += x * y
    }

    println!("{}", total_mul);
}
