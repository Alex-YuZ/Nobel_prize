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
        str. If year or category by comman line input do not exist in original json data, return None.
    """
    data = load_nobel_prizes()
    prizes = data['prizes']
    for prize in prizes:
        if 'laureates' not in prize:
            continue
        if year and prize['year'] != year:
            continue
        if category and prize['category'].lower() != category.lower():
            continue
            
        print("\n====={} Nobel Prize in {}=====".format(prize['year'], prize['category'].title()))
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '')
            print("{} {}: {}\n".format(firstname, surname, laureate['motivation']))
            
if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)