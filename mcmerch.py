import sys

def main():
  
  tax = {"ON" : 0.13}
  # Extract the first argument as the price
  price = float((sys.argv[1]))
  
  # Extract the second argument as the quantity
  quantity = int(sys.argv[2])
  
  pre_tax = price * quantity
  
  after_tax = pre_tax * (1 + tax["ON"])
  
  print(after_tax)
  
if __name__ == '__main__':
  main()