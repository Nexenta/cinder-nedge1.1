#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""Event ID and user visible message mapping.

Event IDs are used to look up the message to be displayed for an API Message
object. All defined messages should be appropriate for any API user to see
and not contain any sensitive information. A good rule-of-thumb is to be very
general in error messages unless the issue is due to a bad user action, then be
specific.
"""

from cinder.i18n import _

UNKNOWN_ERROR = '000001'
UNABLE_TO_ALLOCATE = '000002'
ATTACH_READONLY_VOLUME = '000003'
IMAGE_FROM_VOLUME_OVER_QUOTA = '000004'

event_id_message_map = {
    UNKNOWN_ERROR: _("An unknown error occurred."),
    UNABLE_TO_ALLOCATE: _("No storage could be allocated for this volume "
                          "request. You may be able to try another size or"
                          " volume type."),
    ATTACH_READONLY_VOLUME: _("A readonly volume must be attached as "
                              "readonly."),
    IMAGE_FROM_VOLUME_OVER_QUOTA: _("Failed to copy volume to image as image "
                                    "quota has been met. Please delete images"
                                    " or have your limit increased, then try "
                                    "again."),
}


def get_message_text(event_id):
    return event_id_message_map[event_id]
