{"changed":true,"filter":false,"title":"stack.py","tooltip":"/stack.py","value":"class Stack:\n    def __init__(self):\n        self.items = []\n        \n    def isEmpty(self):\n        return self.items == []\n        \n    def push(self,item):\n        self.items.append(item)\n        \n    def pop(self):\n        return self.items.pop()\n    \n    def peek(self):\n        return self.items[len(self.items)-1]\n        \n    def size(self):\n        return len(self.items)\n        \n        \ndef reverseString(inputString):\n    stack =Stack()\n    \n    i = len(inputString)-1\n    while i>=0:\n       stack.push(inputString[i])\n       i=i-1\n       \n    stack.pop()\n    \n    \nreverseString('roko')\n","undoManager":{"mark":-2,"position":100,"stack":[[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"remove","lines":["k"],"id":1}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"remove","lines":["c"],"id":2}],[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"remove","lines":["a"],"id":3}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"remove","lines":["t"],"id":4}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"remove","lines":["s"],"id":5}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["s"],"id":6}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["t"],"id":7}],[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["a"],"id":8}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["c"],"id":9}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":["k"],"id":10}],[{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["."],"id":11}],[{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["i"],"id":12}],[{"start":{"row":25,"column":21},"end":{"row":25,"column":22},"action":"insert","lines":["t"],"id":13}],[{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["e"],"id":14}],[{"start":{"row":25,"column":23},"end":{"row":25,"column":24},"action":"insert","lines":["m"],"id":15}],[{"start":{"row":25,"column":24},"end":{"row":25,"column":25},"action":"insert","lines":["s"],"id":16}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["{"],"id":17}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"remove","lines":["{"],"id":18}],[{"start":{"row":25,"column":25},"end":{"row":25,"column":26},"action":"insert","lines":["["],"id":19}],[{"start":{"row":25,"column":26},"end":{"row":25,"column":27},"action":"insert","lines":["i"],"id":20}],[{"start":{"row":25,"column":27},"end":{"row":25,"column":28},"action":"insert","lines":["]"],"id":21}],[{"start":{"row":25,"column":28},"end":{"row":25,"column":29},"action":"insert","lines":[")"],"id":22}],[{"start":{"row":25,"column":29},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":26,"column":0},"end":{"row":26,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["i"],"id":24}],[{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["="],"id":25}],[{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["i"],"id":26}],[{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":["-"],"id":27}],[{"start":{"row":26,"column":12},"end":{"row":26,"column":13},"action":"insert","lines":["1"],"id":28}],[{"start":{"row":21,"column":12},"end":{"row":21,"column":15},"action":"remove","lines":["new"],"id":29}],[{"start":{"row":21,"column":12},"end":{"row":21,"column":13},"action":"remove","lines":[" "],"id":30}],[{"start":{"row":21,"column":11},"end":{"row":21,"column":12},"action":"remove","lines":[" "],"id":31}],[{"start":{"row":21,"column":17},"end":{"row":21,"column":34},"action":"remove","lines":["list(inputString)"],"id":32}],[{"start":{"row":21,"column":18},"end":{"row":22,"column":0},"action":"insert","lines":["",""],"id":33},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["s"],"id":34}],[{"start":{"row":22,"column":5},"end":{"row":22,"column":6},"action":"insert","lines":["t"],"id":35}],[{"start":{"row":22,"column":6},"end":{"row":22,"column":7},"action":"insert","lines":["a"],"id":36}],[{"start":{"row":22,"column":7},"end":{"row":22,"column":8},"action":"insert","lines":["c"],"id":37}],[{"start":{"row":22,"column":8},"end":{"row":22,"column":9},"action":"insert","lines":["k"],"id":38}],[{"start":{"row":22,"column":9},"end":{"row":22,"column":10},"action":"insert","lines":["."],"id":39}],[{"start":{"row":22,"column":10},"end":{"row":22,"column":11},"action":"insert","lines":["i"],"id":40}],[{"start":{"row":22,"column":11},"end":{"row":22,"column":12},"action":"insert","lines":["t"],"id":41}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["e"],"id":42}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["m"],"id":43}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["s"],"id":44}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":[" "],"id":45}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":17},"action":"insert","lines":["="],"id":46}],[{"start":{"row":22,"column":17},"end":{"row":22,"column":18},"action":"insert","lines":[" "],"id":47}],[{"start":{"row":22,"column":18},"end":{"row":22,"column":35},"action":"insert","lines":["list(inputString)"],"id":48}],[{"start":{"row":22,"column":35},"end":{"row":22,"column":36},"action":"insert","lines":[";"],"id":49}],[{"start":{"row":24,"column":12},"end":{"row":24,"column":23},"action":"remove","lines":["stack.items"],"id":50},{"start":{"row":24,"column":12},"end":{"row":24,"column":29},"action":"insert","lines":["list(inputString)"]}],[{"start":{"row":22,"column":4},"end":{"row":22,"column":36},"action":"remove","lines":["stack.items = list(inputString);"],"id":51}],[{"start":{"row":22,"column":4},"end":{"row":23,"column":4},"action":"remove","lines":["","    "],"id":52}],[{"start":{"row":25,"column":7},"end":{"row":26,"column":13},"action":"remove","lines":[" print(stack.items[i])","        i=i-1"],"id":53},{"start":{"row":25,"column":7},"end":{"row":25,"column":12},"action":"insert","lines":["stack"]}],[{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["."],"id":54}],[{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["p"],"id":55}],[{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["u"],"id":56}],[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["s"],"id":57}],[{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["h"],"id":58}],[{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["("],"id":59}],[{"start":{"row":23,"column":12},"end":{"row":23,"column":29},"action":"remove","lines":["list(inputString)"],"id":60},{"start":{"row":23,"column":12},"end":{"row":23,"column":23},"action":"insert","lines":["inputString"]}],[{"start":{"row":25,"column":18},"end":{"row":25,"column":29},"action":"insert","lines":["inputString"],"id":61}],[{"start":{"row":25,"column":29},"end":{"row":25,"column":30},"action":"insert","lines":["["],"id":62}],[{"start":{"row":25,"column":30},"end":{"row":25,"column":31},"action":"insert","lines":["i"],"id":63}],[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":["]"],"id":64}],[{"start":{"row":25,"column":32},"end":{"row":25,"column":33},"action":"insert","lines":[")"],"id":65}],[{"start":{"row":25,"column":33},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":66},{"start":{"row":26,"column":0},"end":{"row":26,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":26,"column":7},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":67},{"start":{"row":27,"column":0},"end":{"row":27,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"remove","lines":[" "],"id":68}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"remove","lines":[" "],"id":69}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"remove","lines":[" "],"id":70}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["w"],"id":71}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["h"],"id":72}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["i"],"id":73}],[{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["l"],"id":74}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["e"],"id":75}],[{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["."],"id":76}],[{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"remove","lines":["."],"id":77}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"remove","lines":["e"],"id":78}],[{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"remove","lines":["l"],"id":79}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"remove","lines":["i"],"id":80}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"remove","lines":["h"],"id":81}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"remove","lines":["w"],"id":82}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":5},"action":"insert","lines":["s"],"id":83}],[{"start":{"row":27,"column":5},"end":{"row":27,"column":6},"action":"insert","lines":["t"],"id":84}],[{"start":{"row":27,"column":6},"end":{"row":27,"column":7},"action":"insert","lines":["a"],"id":85}],[{"start":{"row":27,"column":7},"end":{"row":27,"column":8},"action":"insert","lines":["c"],"id":86}],[{"start":{"row":27,"column":8},"end":{"row":27,"column":9},"action":"insert","lines":["k"],"id":87}],[{"start":{"row":27,"column":9},"end":{"row":27,"column":10},"action":"insert","lines":["."],"id":88}],[{"start":{"row":27,"column":10},"end":{"row":27,"column":11},"action":"insert","lines":["p"],"id":89}],[{"start":{"row":27,"column":11},"end":{"row":27,"column":12},"action":"insert","lines":["o"],"id":90}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":13},"action":"insert","lines":["p"],"id":91}],[{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"insert","lines":["("],"id":92}],[{"start":{"row":27,"column":14},"end":{"row":27,"column":15},"action":"insert","lines":[")"],"id":93}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"insert","lines":[";"],"id":94}],[{"start":{"row":27,"column":15},"end":{"row":27,"column":16},"action":"remove","lines":[";"],"id":95}],[{"start":{"row":25,"column":33},"end":{"row":26,"column":0},"action":"insert","lines":["",""],"id":96},{"start":{"row":26,"column":0},"end":{"row":26,"column":7},"action":"insert","lines":["       "]}],[{"start":{"row":26,"column":7},"end":{"row":26,"column":8},"action":"insert","lines":["i"],"id":97}],[{"start":{"row":26,"column":8},"end":{"row":26,"column":9},"action":"insert","lines":["="],"id":98}],[{"start":{"row":26,"column":9},"end":{"row":26,"column":10},"action":"insert","lines":["i"],"id":99}],[{"start":{"row":26,"column":10},"end":{"row":26,"column":11},"action":"insert","lines":["-"],"id":100}],[{"start":{"row":26,"column":11},"end":{"row":26,"column":12},"action":"insert","lines":["1"],"id":101}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":31},"end":{"row":11,"column":31},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1427880015000}