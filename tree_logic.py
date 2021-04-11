# python script to get all nodes
class ParentChildNode():
    def __init__(self):
        self.graph = { 'node_1' : ['4'],
                                'node_2' : ['4'],
                                'node_3' : ['4'],
                                'node_4' : ['5', '7']}
        
    def get_nodes(self, node_value):

        output_dict = {}
        for p_key, p_value in self.graph.items():
            if p_key == node_value:
                child_val = ['node_'+p_value[0]]
                output_dict.setdefault(p_key, []).append(child_val)
                for c_key, c_value in self.graph.items():
                    if c_key == child_val[0]:
                        print(c_value)
                        for i in c_value:
                            i_val = ['node_' + i]
                            print("i_val", i_val)
                            output_dict[p_key].append(i_val)
                output_dict[p_key].append([p_key])
        return output_dict
    
    
if __name__ == '__main__':
    node_value = 'node_1'
    ParentChildNode().get_nodes(node_value)
