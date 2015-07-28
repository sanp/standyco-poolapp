from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
 
def index(request):
  # Tell the base.html template to use the special override_block_content layout
  # rather than the default layout on the rest ofthe pages
  override_block_content = False
  context = {'override_block_content': override_block_content}
  return render(request, 'home/index.html', context)
