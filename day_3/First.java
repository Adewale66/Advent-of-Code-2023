package day_3;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class First {
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
                    if(Character.isDigit(t[i])){
                        int start = i;
                        int end = 0;
                        int j;
                        for (j = i + 1; j < t.length; j++){
                            if (!Character.isDigit(t[j])){
                                end = j;
                                break;
                            }
                        }
                        if (end == 0){
                            end = j;
                        }
                        boolean foundSym = false;
                        for (int l = i; l < end; l++){
                            foundSym = isAdjacent(matrix, k, l);
                            if (foundSym)
                                break;
                        }
                        if (foundSym){
                            int num_of = end - start;
                            int tv = 1;
                            for (int w = 0; w < num_of - 1; w++){
                                tv *= 10;
                            }
                            int number_to_add = 0;
                            while (tv != 0){
                                number_to_add += (Integer.parseInt(String.valueOf(t[start])) * tv);
                                start++;
                                tv /= 10;
                            }
                            total += number_to_add;
                            i = end - 1;
                        }

                    }
                }
            }
            System.out.println(total);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static boolean isAdjacent(List<char[]> array, int row, int col) {
        int numRows = array.size();
        int numCols = array.get(0).length;
        char[] symbols = {'#', '$', '%', '&', '=', '*', '@', '/', '-', '+'};

        for (int i = row - 1; i <= row + 1; i++) {
            for (int j = col - 1; j <= col + 1; j++) {
                if (i >= 0 && i < numRows && j >= 0 && j < numCols) {
                    for (char k : symbols){
                        if (k == array.get(i)[j]){
                            return true;
                        }
                    }
                }
            }
        }

        return false;
    }
}

