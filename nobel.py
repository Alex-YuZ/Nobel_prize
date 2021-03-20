import json
import helper

def load_nobel_prizes(filename='prize.json'):
    """
    Read in the data from external json file
    
    """
    with open(filename) as infile:
        contents = json.load(infile)
    return contents

def main(year, category):
    """
    Print out the results based on command line inputs
    
    Parameters:
    -----------
        year: int. If none, print out results of all recorded years if any (including all categories).
        category: str. If none, print out results of all recorded categories if any (including all years if ).
    
    Returns:
    --------
        str. If year or category by command line input do not exist in original json data, return None.
    """
    data = load_nobel_prizes()
    prizes = data['prizes']
    for prize in prizes:
        
        # If `laureates` does not exist in the current `prize` dict, skip to next iteration.
        if 'laureates' not in prize:
            continue
            
        # If input `year` is not null but does not match the key `year` of current `prize` dict, 
        # then skip to next iteration.
        if year and prize['year'] != year:
            continue
            
        # If input `category` is not null but does not match the key `category` in current `prize` dict, 
        # then skip to next iteration.
        if category and prize['category'].lower() != category.lower():
            continue
        
        # If the three conditions above all failed, execute the following codes and print the query.
        print("\n====={} Nobel Prize in {}=====".format(prize['year'], prize['category'].title()))
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '')
            print("{} {}: {}\n".format(firstname, surname, laureate['motivation']))
            
if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)