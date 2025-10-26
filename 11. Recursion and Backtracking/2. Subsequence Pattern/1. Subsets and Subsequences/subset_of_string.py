class Main(object):
    @staticmethod
    def findSubsets(string, ans, idx):
        if idx == len(string):
            if len(ans) == 0:
                print("NULL")
            else:
                print(ans)
            return
        
        # Include string[idx]
        Main.findSubsets(string, ans + string[idx], idx + 1)
        # Exclude string[idx]
        Main.findSubsets(string, ans, idx + 1)


# Example usage
if __name__ == "__main__":
    string = "abc"
    Main.findSubsets(string, "", 0)
