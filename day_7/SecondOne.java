package day_7;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class PartTwo {
    public static void main(String[] args) {
        try {
            BufferedReader file = new BufferedReader(new FileReader("input"));
            Map<Character, Integer> values = new HashMap<>();

            String line;
            List<String> hands = new ArrayList<>();
            while((line = file.readLine()) != null) {
                String split = line.split(" ")[0];
                for (char c: split.toCharArray())
                    values.put(c, values.getOrDefault(c, 0) + 1);
                String size;
                if (values.containsKey('J')){
                    int jCount = values.get('J');
                    values.remove('J');
                    if (jCount == 5){
                        size = "6";
                        values.clear();
                        hands.add(line + " " + size);
                        continue;
                    }
                    int max = 0;
                    char charac = ' ';
                    for (char c: values.keySet()){
                        if (values.get(c) > max)
                        {
                            max = values.get(c);
                            charac = c;
                        }
                    }
                    values.put(charac, values.get(charac) + jCount);
                }
                int rank = values.size();
                if (rank== 1)
                    size = "6";
                else if (rank == 2 && values.containsValue(4))
                    size = "5";
                else if (rank == 2 && values.containsValue(3) && values.containsValue(2))
                    size = "4";
                else if (rank == 3 && values.containsValue(3))
                    size = "3";
                else if (rank == 3 && values.containsValue(2))
                    size = "2";
                else if (rank == 4)
                    size = "1";
                else
                    size = "0";
                values.clear();
                hands.add(line + " " + size);
            }
            file.close();

            List<Character> strength = Arrays.asList('A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J');
            Collections.reverse(strength);
            for (int i =0; i < hands.size() - 1; i++){
                for (int j = i + 1; j < hands.size(); j++){
                    String[] hand1 = hands.get(i).split(" ");
                    String[] hand2 = hands.get(j).split(" ");
                    if (Integer.parseInt(hand1[2]) > Integer.parseInt(hand2[2])){
                        Collections.swap(hands, i, j);
                    }
                    else if (Integer.parseInt(hand1[2]) == Integer.parseInt(hand2[2])){
                        for (int k = 0; k < hand1[0].length(); k++){
                            if (strength.indexOf(hand1[0].charAt(k)) > strength.indexOf(hand2[0].charAt(k))){
                                Collections.swap(hands, i, j);
                                break;
                            }
                            else if (strength.indexOf(hand1[0].charAt(k)) < strength.indexOf(hand2[0].charAt(k))){
                                break;
                            }
                        }
                    }
                }
            }
            int total = 0;
            int i = 1;
            for (String hand: hands){
                int v = Integer.parseInt(hand.split(" ")[1]);
                total += v * i;
                i++;
            }
            System.out.println(total);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

