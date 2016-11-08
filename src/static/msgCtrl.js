app.controller('msgCtrl', function($scope, view, $timeout) {
    $scope.wsOpen = function(event) {
        console.debug(event);
    };

    $scope.wsMessage = function(event) {
        message = JSON.parse(event.data);
        if (message.act != 7)
            console.debug(message);
        if (message.act === 1) { // JOIN SUCCESSFULLY
            $scope.join_as_watcher(message.name);
        } else if (message.act === 2) {// Initialize 
            $scope.someone_joins(message.nick_id, message.user_type);
        } else if (message.act === 3) {// Someone joins
            $scope.name = message.nick_id;
            $scope.init_player_list(message.data);
        } else if (message.act === 5) {// Someone leaves
            $scope.someone_leaves(message.name);
        } else if (message.act === 7) {// PAINT PLEASE
            $scope.view.update(message);
        }
    };
    $scope.render = function() {
        loop=window.requestAnimationFrame( $scope.render);
        $scope.view.render();
    };

    $scope.join_as_watcher = function(name) {
        $scope.ws.send(JSON.stringify({
            act         : 2,
            room_id     : $scope.roomId,
            nick_id     : $scope.name,
            user_type   : 1
        }));
    };

    $scope.player_list = {};
    $scope.someone_joins = function(name, type) {
        $timeout(function() {
            $scope.player_list[name] = type;
        }, 500);
    };
    $scope.someone_leaves = function(name) {
        $timeout(function() {
            delete $scope.player_list[name];
        }, 500);
    };

    $scope.init_player_list = function(data) {
        $timeout(function() {
            for (var i in data) {
                $scope.player_list[data[i].name]= data[i].user_type;
            }
        }, 500);
    };

    $scope.init = function (wsAddr, roomId, name) {
        $scope.name     = name;
        $scope.roomId   = roomId;
        $scope.view     = view;
        $scope.ws       = new WebSocket(wsAddr);
        $scope.ws.onopen    = $scope.wsOpen;
        $scope.ws.onmessage = $scope.wsMessage;
        $scope.render();
    };
});