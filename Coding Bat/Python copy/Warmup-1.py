def front3(str):
  if len(str) < 3:
    return str*3
  else:
    front = str[:3]
    return front*3
