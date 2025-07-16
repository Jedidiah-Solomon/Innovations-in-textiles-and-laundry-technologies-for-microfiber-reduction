
# By Blessing Odunayo and Jedidiah Solomon
import graphviz

dot = graphviz.Digraph(comment='PRISMA Flow Diagram', format='png')

# Set layout to horizontal and increase size
dot.attr(rankdir='LR', size='15,7', dpi='300')

# Node style: bigger font, bold font, and more padding for readability
dot.attr('node', shape='box', style='filled', fillcolor='lightgrey', fontsize='18', margin='0.5',
         fontname='Arial Bold')

# Define nodes with bold font
dot.node('id1', 'Records identified from:\n- Web of Science (n = 1,728)\n- Medline (n = 544)\n- CSCD (n = 17)\nTotal = 2,289')
dot.node('sc1', 'Duplicates removed (n = 553)')
dot.node('sc2', 'Records after deduplication\n(n = 1,736)')
dot.node('el1', 'Records screened by keyword\n(n = 1,736)')
dot.node('el2', 'Records excluded (n = 484)')
dot.node('inc', 'Records included in final dataset\n(n = 1,252)', fillcolor='lightblue')

# Define edges
dot.edge('id1', 'sc1')
dot.edge('sc1', 'sc2')
dot.edge('sc2', 'el1')
dot.edge('el1', 'el2')
dot.edge('el1', 'inc')

# Render and save
output_path = '/content/prisma_flowchart'
dot.render(output_path, cleanup=True)

output_path + '.png'
