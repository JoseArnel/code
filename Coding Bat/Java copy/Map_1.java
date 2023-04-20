Java Map API

// Make a new empty map
Map<String, String> map = new HashMap<String, String>();
map.get(key) -- retrieves the stored value for a key, or null if that key is not present in the map.

map.put(key, value) -- stores a new key/value pair in the map. Overwrites any existing value for that key.

map.containsKey(key) -- returns true if the key is in the map, false otherwise.

map.remove(key) -- removes the key/value pair for this key if present. Does nothing if the key is not present.

//  mapBully 
public Map<String, String> mapBully(Map<String, String> map) {
    if (map.containsKey("a")) {
      map.put("b", map.get("a"));
      map.put("a", "");
    }
    return map;
  }

  // mapShare 
  public Map<String, String> mapShare(Map<String, String> map) {
    if (map.containsKey("a")){
      map.put("a", map.get("a"));
      map.put("b", map.get("a"));
      map.remove("c");
    }
    else {
      map.put("b", map.get("b"));
      map.remove("c");
    }
    return map;
  }
  
  // mapAB 
  public Map<String, String> mapAB(Map<String, String> map) {
    if (map.containsKey("a") && map.containsKey("b")){
      map.put("ab", map.get("a") + map.get("b"));
    }
    return map;
  }

  // topping1 
  public Map<String, String> topping1(Map<String, String> map) {
    map.put("bread", "butter");
    if (map.containsKey("ice cream")){
        map.put("ice cream", "cherry");
    }
    return map;
  }
  
 // topping2
 public Map<String, String> topping2(Map<String, String> map) {
  if (map.containsKey("ice cream")){
    map.put("yogurt", map.get("ice cream"));
  }
  if (map.containsKey("spinach")){
    map.put("spinach", "nuts");
  }
  return map;
 }

 // topping3
 public Map<String, String> topping3(Map<String, String> map) {
  if (map.containsKey("potato")){
    map.put("fries", map.get("potato"));
  }
  if (map.containsKey("salad")){
    map.put("spinach", map.get("salad"));
  }
  return map;
 }

 // mapAB2
 public Map<String, String> mapAB2(Map<String, String> map) {
  if(map.containsKey("a") && map.containsKey("b")) {
    if(map.get("a").equals(map.get("b"))){
      map.remove("a");
      map.remove("b");
    }
  }
  return map;
 }

 // 
  
  // mapAB3 
 public Map<String, String> mapAB3(Map<String, String> map) {
  if((map.containsKey("a") || map.containsKey("b")) && !(map.containsKey("a") && map.containsKey("b"))){
    if(map.containsKey("a")){
      map.put("b", map.get("a"));
    }
    if(map.containsKey("b")){
      map.put("a", map.get("b"));
    }
  }
  return map;
 }

 // mapAB4
 public Map<String, String> mapAB4(Map<String, String> map) {
  if((map.containsKey("a") && map.containsKey("b")) && (map.get("a").length() == map.get("b").length())){
    map.put("a", "");
    map.put("b", "");
  }
  if((map.containsKey("a") && map.containsKey("b")) && (map.get("a").length() != map.get("b").length())){
    if(map.get("a").length() > map.get("b").length()){
      map.put("c", map.get("a"));
    }
    else{
      map.put("c", map.get("b"));
    }
  }
  return map;
 }

