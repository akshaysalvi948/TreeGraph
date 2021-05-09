# python script to get all nodes
import re
class ParentChildNode():
    def __init__(self):
        self.graph = { 'node_1' : ['4'],
                                'node_2' : ['4'],
                                'node_3' : ['4'],
                                'node_4' : ['5', '7']}
        # 12347
    
    def get_input(self, input_tree):
        # input_val = {"relation": [{"parent": "node_1", "child": "node_4"},
        #                 {"parent": "node_2", "child": "node_4"},
        #                 {"parent": "node_3", "child": "node_4"},
        #                 {"parent": "node_4", "child": "node_5"},
        #                 {"parent": "node_4", "child": "node_7"},
        #                 {"parent": "node_6", "child": "node_5"}],
        #             "node_ids": ["node_5", "node_7", "node_4"]}
        print("input_tree", input_tree["node_ids"])
        
        return input_tree["node_ids"]

    def get_nodes(self, node_value):
        # forward propagation
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
                
            else :
                output_list = self.without_key_nodes(p_key)
                output_dict[p_key].append(output_list)
            
        print(output_dict)      
        return output_dict
    
    def without_key_nodes(self, node_value):
        # output_dict = {}
        node_list = []
        final_list = []
        # rev_graph = reversed( self.graph)
        
        rev_graph = dict(reversed(list(self.graph.items())))
        
        print("rev_graph", rev_graph)
        for p_key, p_value in rev_graph.items():
            new_key = p_key.replace("_", '')
            p_key = [int(new_key[-1])]
            print("p_key", p_key)
            print("_val", p_value)
            if p_key in p_value:
                print("node_num", p_key)
                node_list.append(p_key)
        print("node_list", node_list)
        final_val = sorted(node_list)
        for i in final_val:
            i_val = ['node_' + i]
            final_list.append(i_val)
        final_list.append(node_value)
        
        return final_list
        
            
                # output_dict.setdefault(p_key, []).append(child_val)
                
                
    
    def get_all_nodes():
        # backpropagation logic
        input = "node"
        pass
    
    def ouputs():
        
        # first call fronpagation
        #  if null than run back propagation
        pass
    
    
# if __name__ == '__main__':
#     node_value = 'node_1'
#     ParentChildNode().get_nodes(node_value)
