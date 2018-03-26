import sys

class MyTrieNode:

    def __init__(self, isRootNode):
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mapping each character from a-z to the child node


    def addWord(self,w):

        # base case
        if (len(w) == 0):
            self.count = self.count + 1
            self.isWordEnd = True
            return

        # if key does not exist create it
        if (w[0] not in self.next):
            self.next[w[0]] = MyTrieNode(False)

        # add sub word to next node
        return self.next[w[0]].addWord(w[1:])


    def lookupWord(self,w):

        # base case
        if (len(w) == 0):
            if (self.isWordEnd):
                return self.count
            else:
                return 0

        # letter not in dict
        if (w[0] not in self.next):
            return 0

        # traverse to next node
        return self.next[w[0]].lookupWord(w[1:])


    def autoComplete(self,w):

        # root node case
        if (self.isRoot):

            # find start node
            startNode = self
            for n in w:
                if (n in startNode.next):
                    startNode = startNode.next[n]
                else:
                    return []

            return_list = []
            sub_list = startNode.autoComplete(w)

            # prepend w to sub_list
            for l in sub_list:
                return_list.append((w + l[0], l[1]))

            # return return_list
            return return_list


        # all other nodes
        else:

            # base case (assume an end node is a word end)
            if (len(self.next) == 0):
                return [('', self.count)]

            return_list = []

            # call autoComplete on everynode and prepend previous letter
            for k in self.next:

                sub_list = self.next[k].autoComplete(w)

                for l in sub_list:
                    return_list.append((k + l[0], l[1]))

            # add current word if it is a word end
            if (self.isWordEnd):
                return_list.append(('', self.count))

            # return return_list
            return return_list


if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
