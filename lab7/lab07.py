def main() -> None:
    # Write your file processing code here
    with open('numbers.txt') as f:
        try:
            with open('output.txt', 'w') as t:
                for line in f:
                    ls = line.split()
                    nums = []
                    for element in ls:
                        try:
                            nums.append(int(element))
                        except ValueError:
                            pass
                    if(len(nums)>1):
                        t.write(f'{nums[0]} + {nums[1]} = {nums[0]+nums[1]}\n')
        except FileNotFoundError:
            print("input not found")







if __name__ == '__main__':
    main()
