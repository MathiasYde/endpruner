import os
import click

@click.command()
@click.option("--directory", "--dir", required=True, help="directory to prune region files from")
@click.option("--move", "--m", help="move files instead of deleting them to this directory")
def main(directory, move):
  with open("keep.txt", "r") as file:
    # ignore lines that start with #
    regions = [line.strip() for line in file.readlines() if line[0] != "#"]

  for file in os.listdir(directory):
    if file in regions: continue

    # safe gaurds
    if not file.endswith("mca"):
      print(f"Warning: {file} is not a Minecraft region file. Check if you have the correct directory.")
      continue

    if move:
      os.rename(os.path.join(directory, file), os.path.join(move, file))
    else:
      os.remove(os.path.join(directory, file))

if __name__ == "__main__":
  main()