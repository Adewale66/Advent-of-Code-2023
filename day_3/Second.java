package day_3;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Second {
    public static void main(String[] args){
        try {
            FileReader fileReader = new FileReader("input.txt");
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            List<char []> matrix = new ArrayList<>();
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                matrix.add(line.toCharArray());
            }
            bufferedReader.close();
            fileReader.close();
            int total = 0;
            for (int k = 0; k < matrix.size(); k++){
                char[] t = matrix.get(k);
                for (int i = 0; i <  t.length; i++){
                    if (t[i] == '*'){
                        int gear_ratio = isAdjacent(matrix, k, i);
                        total += gear_ratio;
                    }
                }
            }
            System.out.println(total);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static int isAdjacent(List<char[]> array, int row, int col) {
        int numRows = array.size();
        int numCols = array.get(0).length;
        List<Integer> nums = new ArrayList<>();

        for (int i = row - 1; i <= row + 1; i++) {
            for (int j = col - 1; j <= col + 1; j++) {
                if (i >= 0 && i < numRows && j >= 0 && j < numCols) {
                    if (Character.isDigit(array.get(i)[j])){
                        int x = (getNum(array, i, j));
                        if (!nums.contains(x))
                            nums.add(x);

                    }
                }
            }
        }
        if (nums.size() != 2)
               return 0;
//        System.out.println(nums.get(0));
//        System.out.println(nums.get(1));
        return nums.get(0) * nums.get(1);
    }
    private static int getNum(List<char[]> arr, int row, int col){
        int begin = arr.get(0).length;
        int num_value = 0;
        while (col >= 0 && Character.isDigit(arr.get(row)[col]))
            col--;

        int num_of_digits = 0;
        int temp = ++col;

        while (col < begin && Character.isDigit(arr.get(row)[col]))
        {
            num_of_digits++;
            col++;
        }


        int tv = 1;
        for (int i = 0; i < num_of_digits - 1; i++){
            tv *= 10;
        }
        while (tv != 0){
            num_value += (Integer.parseInt(String.valueOf(arr.get(row)[temp++])) * tv);
            tv /= 10;
        }
        return  num_value;
    }
}

