package day9;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Second {
    public static void main(String[] args) {
        try {
            BufferedReader lines = new BufferedReader(new FileReader("input"));
            String line;
            List<Integer> lastNumbers = new ArrayList<>();
            int total = 0;
            while ((line = lines.readLine()) != null){
                List<Integer> nums = Arrays.stream(line.split(" ")).mapToInt(Integer::parseInt).boxed().toList();
                List<Integer> newNums = new ArrayList<>();
                lastNumbers.add(nums.get(0));

                while (true){
                    for (int i = 1; i < nums.size(); i++) {
                        newNums.add(nums.get(i) - nums.get(i - 1));
                    }
                    lastNumbers.add(newNums.get(0));
                    nums = newNums;
                    newNums = new ArrayList<>();

                    int zero = 0;
                    for (int num : nums){
                        if (num == 0){
                            zero++;
                        }
                    }
                    if (zero == nums.size()){
                        break;
                    }
                }
                Collections.reverse(lastNumbers);
                total += lastNumbers.stream().reduce(0, (a, b) -> b - a);
                lastNumbers.clear();
            }
            System.out.println(total);
        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
