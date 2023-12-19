package day_19;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class First {
    public static void main(String[] args){
        try {
            BufferedReader reader = new BufferedReader(new FileReader("input"));
            Map<String, String> commands = new HashMap<>();
            String line;
            String pos = "in";

            while ((line = reader.readLine()) != null){

                String[] command = line.replace("{", " ").replace("}", "").split(" ");
                if(!line.isEmpty())
                    commands.put(command[0], command[1]);
                else
                    break;
            }
            int total = 0;
            while ((line = reader.readLine()) != null){
                String[] workflow = line.replace("{","").replace("}", "").split(",");
                pos = "in";
                while (!pos.equals("A") && !pos.equals("R")){
                    boolean f = false;
                    String[] cmd = commands.get(pos).split(",");
                    for (String t : cmd){
                        if (t.length() < 4){
                            pos = t;
                            break;
                        }
                        for (String s : workflow){
                            if (t.charAt(0) == s.charAt(0)){
                                int value = Integer.parseInt(s.split("=")[1]);
                                if (t.charAt(1) == '<'){
                                    String[] values = t.split("<")[1].split(":");
                                    int com = Integer.parseInt(values[0]);
                                    if (value < com){
                                        pos = values[1];
                                        f = true;
                                        break;
                                    }
                                }
                                else {
                                    String[] values = t.split(">")[1].split(":");
                                    int com = Integer.parseInt(values[0]);
                                    if (value > com){
                                        pos = values[1];
                                        f = true;
                                        break;
                                    }
                                }
                            }
                        }
                        if (f)
                            break;
                    }
                }
                if (pos.equals("A")){
                    for (String t : workflow){
                        total += Integer.parseInt(t.split("=")[1]);
                    }
                }
            }
            System.out.println(total);

        } catch (IOException e){
            e.printStackTrace();
        }
    }
}
