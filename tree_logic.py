# python script to get all nodes
class ParentChildNode():
    def __init__(self):
        self.graph = { 'node_1' : ['4'],
                                'node_2' : ['4'],
                                'node_3' : ['4'],
                                'node_4' : ['5', '7']}
    
    
    def get_nodes(self, node_value):
        
        # node_value = 'node_1'
        
        all_key = []
        all_val = []
        
        # graph_val = self.graph
        for p_key, p_value in self.graph.items():
            if p_key == node_value:
                child_val = 'node_'+p_value[0]
                all_key = all_key.append(list(p_key))
                all_val = all_val.append(list(child_val))
                
                for c_key, c_value in self.graph.items():            
                    if c_key == child_val:
                        print(c_value)
                        for i in c_value:
                            i_val = ['node_' + i]
                            print("i_val", i_val)
                            all_val = all_val.append(i_val)
                all_val =  all_val.append(list(p_key))
            
        print("all_key", all_key)
        print("all_val", all_val)
        output_dict = dict(zip(all_key, all_val))
        # output_dict["key"] = all_key
        # output_dict["value"] = all_val
        
        print("output_dict", output_dict)
        return all_val
    
if __name__ == '__main__':
    node_value = 'node_1'
    ParentChildNode().get_nodes(node_value)
    
    
    # { "node_1" : ["node_4"], ["node_5"], ["node_7"], ["node_1"]}
