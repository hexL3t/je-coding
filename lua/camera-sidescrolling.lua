-- Add a new LocalScript "CameraManager" inside of StarterPlayer > StarterPlayerScripts

-- Services used to access players, update per frame, and control the camera
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")

local player = Players.LocalPlayer
local camera = workspace.CurrentCamera

-- Camera distance and height offset relative to the player
local CAMERA_DEPTH = 24      -- How far "in front" the camera sits (Z-axis)
local HEIGHT_OFFSET = 2      -- How much higher the camera is (Y-axis)

-- Function to update the camera every frame to follow the player
local function updateCamera()
	local character = player.Character
	if character then
		local root = character:FindFirstChild("HumanoidRootPart")
		if root then
			-- Position the camera at a fixed Z distance from the player
			local rootPosition = root.Position + Vector3.new(0, HEIGHT_OFFSET, 0)
			local cameraPosition = Vector3.new(rootPosition.X, rootPosition.Y, CAMERA_DEPTH)
			
			-- Look at the player's center from the side
			camera.CFrame = CFrame.lookAt(cameraPosition, rootPosition)
		end
	end
end

-- Run the update function every frame, just after the default camera update
RunService:BindToRenderStep("SidescrollingCamera", Enum.RenderPriority.Camera.Value + 1, updateCamera)
