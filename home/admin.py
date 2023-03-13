# Copyright 2023 John Macdonald, Elena Xu, Jonathan Lo, Gurkirat Singh, and Geoffery Banh

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#         http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Authors)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Liked)
admin.site.register(Inbox)
admin.site.register(Followers)
admin.site.register(Follow)
admin.site.register(Comment)
