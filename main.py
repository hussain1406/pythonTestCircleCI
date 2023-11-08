def add(*nums: int):
    if len(nums) == 2:
        return nums[0] + nums[1]
    return nums[0] + add(*nums[1:])

def print_name(name: str = None):
    if not name:
        name = "Python"
        
    print(f"Hello {name}!")

if __name__ == "__main__":
    print_name()
