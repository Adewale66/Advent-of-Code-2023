package day_19;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class First {
    public static void main(String[] args){
        try {
            BufferedReader reader = new BufferedReader(new FileReader("input"));
            String line;
            List<String[]> grid = new ArrayList<>();
            List<int[]> pos = new ArrayList<>();

            while ((line = reader.readLine()) != null){
                grid.add(line.split(""));
            }
            for (int i = 0; i < grid.size(); i++){
                for (int j = 0; j < grid.get(i).length; j++){
                    if (grid.get(i)[j].equals("S")){
                        pos.add(new int[]{i, j});
                    }
                }
            }
            int steps = 64;

            while (steps != 0){
                int size = pos.size();
                while (size-- != 0){
                    int[] temp = pos.remove(0);
                    int x = temp[0];
                    int y = temp[1];

                    if (x + 1 < grid.size() && grid.get(x + 1)[y].equals(".")){
                        grid.get(x + 1)[y] = "O";
                        pos.add(new int[]{x + 1, y});
                    }
                    if (x - 1 >= 0 && grid.get(x - 1)[y].equals(".")){
                        grid.get(x - 1)[y] = "O";
                        pos.add(new int[]{x - 1, y});
                    }
                    if (y + 1 < grid.get(x).length && grid.get(x)[y + 1].equals(".")){
                        grid.get(x)[y + 1] = "O";
                        pos.add(new int[]{x, y + 1});
                    }
                    if (y - 1 >= 0 && grid.get(x)[y - 1].equals(".")){
                        grid.get(x)[y - 1] = "O";
                        pos.add(new int[]{x, y - 1});
                    }
                    grid.get(x)[y] = ".";
                }
                steps--;
            }
            int count = 0;
            for (String[] s: grid){
                for (String t: s){
                    if (t.equals("O"))
                        count++;
                }
            }
            System.out.println(count);

        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
