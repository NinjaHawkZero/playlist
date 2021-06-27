"""Forms for playlist app."""

from wtforms import SelectField, StringField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    # Add the necessary code to use this form
    name = StringField("Playlist Name", validators=[InputRequired()])
    description = StringField("Playlist Description", validators=[InputRequired()])


class SongForm(FlaskForm):
    """Form for adding songs."""

    # Add the necessary code to use this form
    title = StringField("Song Name", validators=[InputRequired()])
    artist = StringField("Song Description", validators=[InputRequired()])



# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
