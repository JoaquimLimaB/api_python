from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        model_permission_codename = self.get_model_permission_codename(
                method= request.method,
                view = view,
            )
        
        if not model_permission_codename:
            return False
        
        return request.user.has_perm(model_permission_codename)     
   
    #Função para capturar o nome da app e do model  e return a string dinamica no formato correto ex: {genres}.{view}_{genre}
    def get_model_permission_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_label = view.queryset.model._meta.app_label
            action = self.get_action_sufix(method)
            return f'{app_label}.{action}_{model_name}'
        except AttributeError:
            return None
    
    #Função para capturar o nome da ação(ex: delete, view)
    def get_action_sufix(self, method):
        method_actions = { 
            'GET': 'view', 
            'POST': 'add', 
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete', 
            'OPTIONS': 'view', 
            'HEAD': 'view', 
            }
        return method_actions.get(method, '')