// FoxPlayer Node.JS server

'use strict';

var express = require('express');
var bodyParser = require('body-parser');

var app = express();

app.use(bodyParser.json());

// DB mock
var tracks = [
    { "id": 21, "title": "Halahula", "artist": "Untitled artist", "duration": 545, "path": "c:/music/halahula.mp3" },
    { "id": 412, "title": "No sleep till Brooklyn", "artist": "Beastie Boys", "duration": 312.12, "path": "c:/music/beastie boys/No sleep till Brooklyn.mp3" }
];
var playlists = [
  { "playlist_id": 0, "name": "Favorites", "tracks": [] },
  { "playlist_id": 1, "name": "Music for coding", "tracks":[21, 412]},
];


// *** Endpoints ***

// PLAYLISTS

// List all the playlists
app.get('/playlists', function listAllTracks(req, res) {
  res.json(playlists);
});

// Create playlist
app.post('/playlists', function (req, res) {
  var playlistName = req.body.playlist;
  // NOTE: Mocked version, no DB
  playlists.push({
      "playlist_id": playlists.length,
      "name": playlistName,
      "tracks": []
  });

  res.json(playlists);
});

// Delete playslist
app.delete('/playlists/:id', function (req, res) {
  // req: playlist id
  // ! Can't delete system playlist
  // ERR: if id missing or not enum., error in JSON (why?)
});

// PLAYLIST tracks
// List all tracks
app.get('/playlist-tracks/', function (req, res) {
  // no id: all tracks in root folder
  // list playlist tracks
});

// List playlist tracks
app.get('/playlist-tracks/:playlist_id', function (req, res) {
  // list all trakcs in playlist
});

// Add track to playlist
app.post('/playlist-tracks/:playlist_id', function (req, res) {
  // add track to playlist
});

// Delete track from playlist
app.delete('/playlist-tracks/:playlist_id/:track_id', function (req, res) {
  // list all trakcs in playlist
  // missing or not enumerable id: JSON error
});


app.listen(3000, function logServerStatus() {
  console.log('FoxPlayer server up and running on localhost:3000');
});
