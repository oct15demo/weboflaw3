'''
Created on Jun 30, 2020

@author: charles
'''

''' Emulate one line shell script used to call run_citation_graph_on_directory_list.py
    shell script run_on_scotus consists of the following line:
    python3.6 run_citation_graph_on_directory_list.py scotus.list scotus_c 
    
    xattr -d com.apple.quarantine my_jar.jar
    xattr -c chartdir_cpp_mac.tar.gz 
    makecsv3.py            try encoding to file open line 587
    coreference3.py        f_line = instream.read(encoding='utf-8') line 678 
       "                   with open(out_graph,'w') as f_citation_graph,open(global_table_file,'w', encoding='utf-8') as f_global_citations: line 1003
       "                   with open(out_file,'w', encoding='utf-8') as outstream: line 550'''
      
import run_citation_graph_on_directory_list as run_cite_graph

def main():
    import cProfile
    #cProfile.run('foo()')
    cProfile.run('run_cite_graph.main([__name__, "scotus.list", "scotus_c"])');

if __name__ == '__main__':
    main()
